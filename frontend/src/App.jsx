import { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  async function fetchMessage() {
    try {
      // Adjust the URL if necessary. In production, you'll have a unified domain.
      // const response = await fetch('http://127.0.0.1:8000/');
      const response = await fetch('/api/');
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error fetching message:', error);
    }
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1>React Frontend</h1>
      <button onClick={fetchMessage}>Fetch Backend Message</button>
      {message && <p>Backend says: {message}</p>}
    </div>
  );
}

export default App;
