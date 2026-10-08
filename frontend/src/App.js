import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Cases from './pages/Cases';
import Wallet from './pages/Wallet';
import Timeline from './pages/Timeline';
import Evidence from './pages/Evidence';
export default function App() {
    return (_jsxs(BrowserRouter, { children: [_jsxs("nav", { style: { display: 'flex', gap: 12 }, children: [_jsx(Link, { to: "/", children: "Cases" }), _jsx(Link, { to: "/wallet", children: "Wallet" }), _jsx(Link, { to: "/timeline", children: "Timeline" }), _jsx(Link, { to: "/evidence", children: "Evidence" }), _jsx("span", { style: { marginLeft: 'auto' }, children: "REPLAY badge | CANNED demo" })] }), _jsxs(Routes, { children: [_jsx(Route, { path: "/", element: _jsx(Cases, {}) }), _jsx(Route, { path: "/wallet", element: _jsx(Wallet, {}) }), _jsx(Route, { path: "/timeline", element: _jsx(Timeline, {}) }), _jsx(Route, { path: "/evidence", element: _jsx(Evidence, {}) })] })] }));
}
