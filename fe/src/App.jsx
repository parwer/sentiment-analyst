import { useState } from "react";
import './app.css'

function App() {
  const [messages, setMessages] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers:{
        'Content-Type': 'application/json',
      } ,
      body: JSON.stringify({message:messages})
    }
    ).then(res => res.json())
      .then(data => { console.log(data) })
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          Message
          <input type="text" value={messages} onChange={e => setMessages(e.target.value)}/>
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default App;