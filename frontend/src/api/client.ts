export async function trace(address: string) {
  const r = await fetch('http://localhost:8000/trace', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ address }),
  });
  return r.json();
}
export async function exportPacket(caseId: string) {
  const r = await fetch(`http://localhost:8000/export/sahyog-packet.json?case_id=${caseId}`);
  return r.json();
}
