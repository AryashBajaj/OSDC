import React, { useEffect, useState } from "react";
import api from "../api";
import "../styles/Note.css";

function Message({ message, onDelete }) {
  const formattedDate = new Date(message.created_at).toLocaleDateString(
    "en-US"
  );
  const uid = message.author;

  const [user, setUser] = useState({});

  useEffect(() => {
    getUser();
  }, []);

  const getUser = () => {
    api
      .get(`/forum/getUser/${uid}`)
      .then((res) => res.data)
      .then((data) => setUser(data))
      .catch((err) => alert(err));
  };

  return (
    <div className="">
      <p className="">{message.title}</p>
      <p className="">{message.content}</p>
      <p className="">{formattedDate}</p>
      <button className="" onClick={() => onDelete(message.id)}>
        Delete
      </button>
    </div>
  );
}

export default Message;
