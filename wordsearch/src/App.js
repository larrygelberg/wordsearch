import React, { useState, useRef, useEffect } from "react";

export default function App() {
  const canvasRef = useRef(null);

  const [grid, setGrid] = useState([]);
  const [words, setWords] = useState([]);
  const [ovals, setOvals] = useState([]);
  const [selection, setSelection] = useState(null);

  const [cellSize, setCellSize] = useState(40);
  const [fontSize, setFontSize] = useState(20);
  const [showOverlay, setShowOverlay] = useState(false);

  // --- scaling ---
  const computeScaling = (parsedGrid) => {
    if (!parsedGrid || !parsedGrid.length) return;
    const cols = parsedGrid[0].length;
    const rows = parsedGrid.length;
    const maxWidth = window.innerWidth * 0.75;
    const maxHeight = window.innerHeight * 0.75;
    const cellW = Math.floor(maxWidth / cols);
    const cellH = Math.floor(maxHeight / rows);
    const newCell = Math.min(50, Math.min(cellW, cellH));
    const newFont = Math.min(28, Math.max(12, Math.floor(newCell * 0.55)));
    setCellSize(newCell);
    setFontSize(newFont);
  };

  // --- grid upload ---
  const handleGridUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const text = await file.text();
    const lines = text.split(/\r?\n/).filter(line => line.length > 0);

    // keep spaces as valid cells
    const parsedGrid = lines.map(line => line.replace(/\r$/, '').split(''));

    // check rectangular
    const width = parsedGrid[0].length;
    if (!parsedGrid.every(r => r.length === width)) {
      alert("grid.txt rows must all have the same number of characters (spaces count)");
      return;
    }

    computeScaling(parsedGrid);
    setGrid(parsedGrid);
    setOvals([]);
    setWords(prev => prev.map(w => ({ ...w, found: false })));
    setShowOverlay(false);
  };

  // --- word upload ---
  const handleWordsUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const text = await file.text();
    const list = text.split(/\r?\n/).map(l => l.trim()).filter(Boolean).map(w => w.toUpperCase());
    const sorted = list.sort((a, b) => a.length - b.length);
    setWords(sorted.map(w => ({ word: w, found: false })));
    setOvals([]);
    setShowOverlay(false);
  };

  // --- convert mouse to cell ---
  const getCellFromMouse = (e) => {
    const canvas = canvasRef.current;
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();
    const px = e.clientX - rect.left;
    const py = e.clientY - rect.top;
    const x = Math.floor(px / cellSize);
    const y = Math.floor(py / cellSize);
    return { x, y };
  };

  // --- selection ---
  const handleMouseDown = (e) => {
    if (!grid.length) return;
    const c = getCellFromMouse(e);
    if (!c) return;
    const x = Math.max(0, Math.min(grid[0].length - 1, c.x));
    const y = Math.max(0, Math.min(grid.length - 1, c.y));
    setSelection({ start: { x, y }, end: { x, y } });
  };

  const handleMouseMove = (e) => {
    if (!selection) return;
    const c = getCellFromMouse(e);
    if (!c) return;
    const x = Math.max(0, Math.min(grid[0].length - 1, c.x));
    const y = Math.max(0, Math.min(grid.length - 1, c.y));
    setSelection({ ...selection, end: { x, y } });
  };

  const handleMouseUp = (e) => {
    if (!selection) return;
    const start = selection.start;
    const end = selection.end;

    const dx = Math.sign(end.x - start.x);
    const dy = Math.sign(end.y - start.y);
    const length = Math.max(Math.abs(end.x - start.x), Math.abs(end.y - start.y)) + 1;

    const selectedCells = [];
    for (let i = 0; i < length; i++) {
      const cx = start.x + i * dx;
      const cy = start.y + i * dy;
      if (cy >= 0 && cy < grid.length && cx >= 0 && cx < grid[0].length) {
        selectedCells.push({ x: cx, y: cy });
      }
    }

    const selectedWord = selectedCells.map(c => grid[c.y][c.x]).join('');
    const selectedWordRev = selectedWord.split('').reverse().join('');

    const idx = words.findIndex(w => !w.found && (w.word === selectedWord || w.word === selectedWordRev));
    if (idx >= 0) {
      const updated = [...words];
      updated[idx] = { ...updated[idx], found: true };
      setWords(updated);

      const x0 = start.x * cellSize + cellSize / 2;
      const y0 = start.y * cellSize + cellSize / 2;
      const x1 = end.x * cellSize + cellSize / 2;
      const y1 = end.y * cellSize + cellSize / 2;
      const angle = Math.atan2(y1 - y0, x1 - x0);

      setOvals(prev => [...prev, { start, end, angle }]);
    }

    setSelection(null);
  };

  // --- draw ---
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || !grid.length) return;
    const ctx = canvas.getContext("2d");

    const cols = grid[0].length;
    const rows = grid.length;
    canvas.width = cols * cellSize;
    canvas.height = rows * cellSize;
    canvas.style.width = `${Math.min(window.innerWidth * 0.75, cols * cellSize)}px`;
    canvas.style.height = `${Math.min(window.innerHeight * 0.75, rows * cellSize)}px`;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // letters
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = `${fontSize}px monospace`;
    ctx.fillStyle = "black";
    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        const cell = grid[y][x];
        const cx = x * cellSize + cellSize / 2;
        const cy = y * cellSize + cellSize / 2;
        if (cell !== ' ') ctx.fillText(cell, cx, cy);
      }
    }

    // found ovals
    ovals.forEach(ov => {
      const x0 = ov.start.x * cellSize + cellSize / 2;
      const y0 = ov.start.y * cellSize + cellSize / 2;
      const x1 = ov.end.x * cellSize + cellSize / 2;
      const y1 = ov.end.y * cellSize + cellSize / 2;
      const centerX = (x0 + x1) / 2;
      const centerY = (y0 + y1) / 2;
      const dx = x1 - x0;
      const dy = y1 - y0;
      const length = Math.sqrt(dx * dx + dy * dy) + cellSize * 0.5;

      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.rotate(ov.angle);
      ctx.beginPath();

      const radius = cellSize / 2;
      const rectLength = length - radius;

      // Draw the pill shape
      ctx.moveTo(-rectLength / 2, -radius);
      ctx.lineTo(rectLength / 2, -radius);
      ctx.arc(rectLength / 2, 0, radius, -Math.PI / 2, Math.PI / 2);
      ctx.lineTo(-rectLength / 2, radius);
      ctx.arc(-rectLength / 2, 0, radius, Math.PI / 2, -Math.PI / 2);
      ctx.closePath();

      ctx.fillStyle = "rgba(0,128,0,0.3)";
      ctx.fill();
      ctx.restore();

    });

    // selection outline
    if (selection) {
      const s = selection.start;
      const e = selection.end;
      const x0 = s.x * cellSize + cellSize / 2;
      const y0 = s.y * cellSize + cellSize / 2;
      const x1 = e.x * cellSize + cellSize / 2;
      const y1 = e.y * cellSize + cellSize / 2;
      const centerX = (x0 + x1) / 2;
      const centerY = (y0 + y1) / 2;
      const dx = x1 - x0;
      const dy = y1 - y0;
      const length = Math.sqrt(dx * dx + dy * dy) + cellSize * 0.5;
      const angle = Math.atan2(dy, dx);

      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.rotate(angle);
      ctx.beginPath();

      const radius = cellSize / 2;
      const rectLength = length - radius;

      // Draw the pill shape
      ctx.moveTo(-rectLength / 2, -radius);
      ctx.lineTo(rectLength / 2, -radius);
      ctx.arc(rectLength / 2, 0, radius, -Math.PI / 2, Math.PI / 2);
      ctx.lineTo(-rectLength / 2, radius);
      ctx.arc(-rectLength / 2, 0, radius, Math.PI / 2, -Math.PI / 2);
      ctx.closePath();

      ctx.strokeStyle = "rgba(255,0,0,0.6)";
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.restore();

    }

  }, [grid, ovals, selection, cellSize, fontSize]);

  // --- overlay ---
  useEffect(() => {
    if (words.length > 0 && words.every(w => w.found)) setShowOverlay(true);
  }, [words]);

  // resize
  useEffect(() => {
    const onResize = () => { if (grid.length) computeScaling(grid); };
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, [grid]);

  const dismissOverlay = () => setShowOverlay(false);

  return (
    <div style={{ position: "relative", padding: 16, display: "flex", gap: 20 }}>
      <div>
        <div style={{ marginBottom: 8 }}>
          <label style={{ marginRight: 10 }}>
            Load grid.txt
            <input type="file" accept=".txt" onChange={handleGridUpload} style={{ display: "inline-block", marginLeft: 8 }} />
          </label>
          <label>
            Load words.txt
            <input type="file" accept=".txt" onChange={handleWordsUpload} style={{ display: "inline-block", marginLeft: 8 }} />
          </label>
        </div>

        <canvas
          ref={canvasRef}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          style={{ border: "none", display: "block", touchAction: "none" }}
        />
      </div>

      <div>
        <h3>Words to find</h3>
        <ul style={{ marginTop: 0 }}>
          {words.map((w, i) => (
            <li key={i} style={{ textDecoration: w.found ? "line-through" : "none", color: w.found ? "#777" : "#000" }}>
              {w.word}
            </li>
          ))}
        </ul>
      </div>

      {showOverlay && (
        <div style={{
          position: "fixed",
          inset: 0,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "rgba(0,0,0,0.5)",
          zIndex: 9999
        }}>
          <div style={{ background: "white", padding: 24, borderRadius: 8, textAlign: "center" }}>
            <div style={{ fontSize: 32, fontWeight: "700" }}>Yay! You did it!</div>
            <button onClick={dismissOverlay} style={{ marginTop: 16, fontSize: 16, padding: "8px 16px" }}>Dismiss</button>
          </div>
        </div>
      )}
    </div>
  );
}
