import React, { useState, useRef } from 'react';
import './App.css';

const defaultGrid = [
  ['C','A','T','S'],
  ['D','O','G','S'],
  ['B','I','R','D'],
  ['F','I','S','H']
];

const defaultWords = ['CATS','DOGS','BIRD','FISH'];

function App() {
  const [grid, setGrid] = useState(defaultGrid);
  const [words, setWords] = useState(defaultWords.map(w => ({ word: w, found: false })));
  const [ovals, setOvals] = useState([]);
  const canvasRef = useRef(null);
  const [selection, setSelection] = useState(null);

  const cellSize = 50;

  const handleMouseDown = (e) => {
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

      setOvals([...ovals, {...selection}]);
    }

    setSelection(null);
  };

  const drawCanvas = () => {
    const canvas = canvasRef.current;
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

    // draw previous ovals
    ctx.strokeStyle = 'rgba(0,128,0,0.7)';
    ctx.lineWidth = 4;
    ovals.forEach(sel => {
      const x0 = sel.start.x*cellSize + cellSize/2;
      const y0 = sel.start.y*cellSize + cellSize/2;
      const x1 = sel.end.x*cellSize + cellSize/2;
      const y1 = sel.end.y*cellSize + cellSize/2;
      ctx.beginPath();
      ctx.ellipse((x0+x1)/2, (y0+y1)/2, Math.abs(x1-x0)/2 + cellSize/2, Math.abs(y1-y0)/2 + cellSize/2, 0, 0, 2*Math.PI);
      ctx.stroke();
    });

    // draw current selection
    if(selection){
      const x0 = selection.start.x*cellSize + cellSize/2;
      const y0 = selection.start.y*cellSize + cellSize/2;
      const x1 = selection.end.x*cellSize + cellSize/2;
      const y1 = selection.end.y*cellSize + cellSize/2;
      ctx.strokeStyle = 'rgba(255,0,0,0.5)';
      ctx.beginPath();
      ctx.ellipse((x0+x1)/2, (y0+y1)/2, Math.abs(x1-x0)/2 + cellSize/2, Math.abs(y1-y0)/2 + cellSize/2, 0,0,2*Math.PI);
      ctx.stroke();
    }
  };

  React.useEffect(drawCanvas, [grid, ovals, selection]);

  return (
    <div style={{display:'flex', padding:'20px'}}>
      <canvas
        ref={canvasRef}
        width={grid[0].length*cellSize}
        height={grid.length*cellSize}
        style={{border:'1px solid black'}}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
      />
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
    </div>
  );
}

export default App;
