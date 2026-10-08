import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Cases from './pages/Cases';
import Wallet from './pages/Wallet';
import Timeline from './pages/Timeline';
import Evidence from './pages/Evidence';

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ display: 'flex', gap: 12 }}>
        <Link to="/">Cases</Link><Link to="/wallet">Wallet</Link>
        <Link to="/timeline">Timeline</Link><Link to="/evidence">Evidence</Link>
        <span style={{ marginLeft: 'auto' }}>REPLAY badge | CANNED demo</span>
      </nav>
      <Routes>
        <Route path="/" element={<Cases />} />
        <Route path="/wallet" element={<Wallet />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/evidence" element={<Evidence />} />
      </Routes>
    </BrowserRouter>
  );
}
