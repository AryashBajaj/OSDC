import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../api";

function Question() {
  const [isLoading, setIsLoading] = useState(false);
  const [answers, setAnswers] = useState([]);
  const [content, setContent] = useState("");
  const [img, setImg] = useState("");

  console.log(answers);

  const { qid } = useParams();

  useEffect(() => {
    getAnswers(qid);
  }, []);

  const getAnswers = (qid) => {
    api
      .get(`/forum/question/answer/${qid}/`)
      .then((res) => res.data)
      .then((data) => setAnswers(data))
      .catch((err) => alert(err));
  };

}

export default Question;
