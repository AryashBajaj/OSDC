import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api";
import Message from "../components/Message";
import "../styles/Home.css"

function Channel() {
  const [messages, setMessages] = useState([]);
  const [content, setContent] = useState("");

  useEffect(() => {
    getMessages();
  }, []);

  const { cid } = useParams();

  const getMessages = () => {
    api
      .get(`/server/channel/${cid}/message/`)
      .then((res) => res.data)
      .then((data) => {
        setMessages(data);
        console.log(data);
      })
      .catch((err) => alert(err));
  };

  const deleteMessage = (id) => {
    api
      .delete(`/server/message/${id}/`)
      .then((res) => {
        if (res.status === 204) {
          alert("Message succesfully deleted!");
        } else {
          alert("Failed to delete!");
        }
        getMessages();
      })
      .catch((error) => alert(error));
  };

  const createMessage = (e) => {
    e.preventDefault();
    api
      .post(`/server/channel/${cid}/message/`, { content })
      .then((res) => {
        if (res.status === 201) {
          alert("Note created.");
        } else {
          alert("Failed to create");
        }
        getNotes();
      })
      .catch((error) => alert(error));
  };

  return (
    <div>
      <div>
        <h2>Messages</h2>
        {messages.map((message) => (
          <Message message={message} onDelete={deleteMessage} key={message.id} />
        ))}
      </div>
      <h2>Create a Message</h2>
      <form onSubmit={createMessage}>
        <label htmlFor="content">Content:</label>
        <br />
        <textarea
          id="content"
          name="content"
          required
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
        <br />
        <input type="submit" value="Submit"></input>
      </form>
    </div>
  );
}

export default Channel;
