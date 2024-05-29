import React from "react";
import { useEffect, useState } from "react";
import api from "../api";

function QuestionItem({ question }) {
  const uid = question.author;

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

  console.log(user);
  console.log(question);

  return (
    <div className="card mb-3">
      {question.img && (
        <img src={question.img} className="card-img-top" alt="..." />
      )}
      <div className="card-body">
        <h5 className="card-title">{question.title}</h5>
        <p className="card-text">{question.content}</p>
        <p className="card-text">
          <small className="text-body-secondary">
            By {user.username} on {new Date(question.created_at).toGMTString()}
          </small>
        </p>
      </div>
    </div>
  );
}

export default QuestionItem;
