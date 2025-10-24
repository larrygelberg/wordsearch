import React, { useState, useRef } from 'react';
import './App.css';

const cellSize = 50;

function App() {
  const [grid, setGrid] = useState([]);
  const [words, setWords] = useState([]);
  const [ovals, setOvals] = useState([]);
  const canvasRef = useRef(null);
  const [selection, setSelection] = useState(null);

  // --- File readers ---
  const handleGridUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const lines = event.target.result.split(/\r?\n/).filter(line => line.trim() !== '');
      const parsedGrid = lines.map(line => line.trim().toUpperCase().split(''));
      setGrid(parsedGrid);
      setOvals([]);
    };
    reader.readAsText(file);
  };

  const handleWordsUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const lines = event.target.result.split(/\r?\n/).filter(line => line.trim() !== '');
      setWords(lines.map(w => ({ word: w.toUpperCase(), found: false })));
    };
    reader.readAsText(file);
  };

  // --- Canvas interaction ---
  const handleMouseDown = (e) => {
    if (!grid.length) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const x = Math.floor((e.clientX - rect.left) / cellSize);
    const y = Math.floor((e.clientY - rect.top) / cellSize);
    setSelection({ start: {x,y}, end: {x,y} });
  };

  const handleMouseMove = (e) => {
    if (!selection) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const x = Math.floor((e.clientX - rect.left) / cellSize);
    const y = Math.floor((e.clientY - rect.top) / cellSize);
    setSelection({...selection, end:{x,y}});
  };

  const handleMouseUp = () => {
    if (!selection) return;

    const start = selection.start;
    const end = selection.end;

    const selectedCells = [];
    const dx = Math.sign(end.x - start.x);
    const dy = Math.sign(end.y - start.y);
    const length = Math.max(Math.abs(end.x - start.x), Math.abs(end.y - start.y)) + 1;

    for(let i=0;i<length;i++){
      const cx = start.x + i*dx;
      const cy = start.y + i*dy;
      if(cy >=0 && cy < grid.length && cx >=0 && cx < grid[0].length){
        selectedCells.push({x:cx,y:cy});
      }
    }

    const selectedWord = selectedCells.map(c => grid[c.y][c.x]).join('');
    const selectedWordRev = selectedWord.split('').reverse().join('');

    const wordIndex = words.findIndex(w => !w.found && (w.word === selectedWord || w.word === selectedWordRev));
    if(wordIndex >=0){
      const newWords = [...words];
      newWords[wordIndex].found = true;
      setWords(newWords);

      const angle = Math.atan2(end.y - start.y, end.x - start.x);
      setOvals([...ovals, {start, end, angle}]);
    }

    setSelection(null);
  };

  // --- Draw canvas ---
  const drawCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas || !grid.length) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,canvas.width,canvas.height);

    // draw letters
    ctx.font = "24px monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    for(let y=0;y<grid.length;y++){
      for(let x=0;x<grid[0].length;x++){
        ctx.strokeStyle = 'black';
        ctx.strokeRect(x*cellSize, y*cellSize, cellSize, cellSize);
        ctx.fillStyle = 'black';
        ctx.fillText(grid[y][x], x*cellSize + cellSize/2, y*cellSize + cellSize/2);
      }
    }

    // draw previous ovals (filled for found words)
    ovals.forEach(sel => {
      const x0 = sel.start.x*cellSize + cellSize/2;
      const y0 = sel.start.y*cellSize + cellSize/2;
      const x1 = sel.end.x*cellSize + cellSize/2;
      const y1 = sel.end.y*cellSize + cellSize/2;

      const centerX = (x0 + x1)/2;
      const centerY = (y0 + y1)/2;
      const width = Math.sqrt((x1 - x0)**2 + (y1 - y0)**2)/2 + cellSize/2;
      const height = cellSize/1.5;
      const angle = sel.angle;

      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.rotate(angle);

      // Filled oval with 30% transparency
      ctx.fillStyle = 'rgba(0,128,0,0.3)';
      ctx.beginPath();
      ctx.ellipse(0, 0, width, height, 0, 0, 2*Math.PI);
      ctx.fill();

      // Optional: keep stroke outline if you like
      //ctx.strokeStyle = 'rgba(0,128,0,0.7)';
      //ctx.lineWidth = 2;
      //ctx.stroke();

      ctx.restore();
    });

    // draw current selection
    if(selection){
      const x0 = selection.start.x*cellSize + cellSize/2;
      const y0 = selection.start.y*cellSize + cellSize/2;
      const x1 = selection.end.x*cellSize + cellSize/2;
      const y1 = selection.end.y*cellSize + cellSize/2;

      const centerX = (x0 + x1)/2;
      const centerY = (y0 + y1)/2;
      const width = Math.sqrt((x1 - x0)**2 + (y1 - y0)**2)/2 + cellSize/2;
      const height = cellSize/1.5;
      const angle = Math.atan2(y1 - y0, x1 - x0);

      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.rotate(angle);
      ctx.strokeStyle = 'rgba(255,0,0,0.5)';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.ellipse(0,0,width,height,0,0,2*Math.PI);
      ctx.stroke();
      ctx.restore();
    }
  };

  React.useEffect(drawCanvas, [grid, ovals, selection]);

  const allFound = words.length > 0 && words.every(w => w.found);

  return (
    <div style={{position:'relative', display:'flex', padding:'20px'}}>
      <div>
        <div>
          <label>Upload grid file: </label>
          <input type="file" accept=".txt" onChange={handleGridUpload} />
        </div>
        <div style={{marginTop:'10px'}}>
          <label>Upload word file: </label>
          <input type="file" accept=".txt" onChange={handleWordsUpload} />
        </div>
        <canvas
          ref={canvasRef}
          width={(grid[0]?.length || 0)*cellSize}
          height={(grid.length)*cellSize}
          style={{border:'1px solid black', display:'block', marginTop:'10px'}}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
        />
      </div>
      <div style={{marginLeft:'20px'}}>
        <h3>Words to find</h3>
        <ul>
          {words.map(w => (
            <li key={w.word} style={{textDecoration: w.found ? 'line-through' : 'none'}}>
              {w.word}
            </li>
          ))}
        </ul>
      </div>

      {/* Overlay when all words found */}
      {allFound && (
        <div style={{
          position: 'absolute',
          top: 0, left: 0,
          width: '100%',
          height: '100%',
          backgroundColor: 'rgba(0,0,0,0.5)',
          display:'flex',
          justifyContent:'center',
          alignItems:'center',
          color:'white',
          fontSize:'48px',
          fontWeight:'bold',
          zIndex: 10
        }}>
          Yay! You did it!
        </div>
      )}
    </div>
  );
}

export default App;
