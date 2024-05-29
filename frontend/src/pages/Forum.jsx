import { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";
import { QUERY } from "../constants";
import LoadingIndicator from "../components/LoadingIndicator";
import api from "../api";
import QuestionItem from "../components/QuestionItem";

function Forum() {
  const [isLoading, setIsLoading] = useState(false);
  const [query, setQuery] = useState("");
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    getQuestions();
  }, []);

  console.log(questions);

  const getQuestions = () => {
    setIsLoading(true);
    setQuery(localStorage.getItem(QUERY));
    if (query === "") {
      api
        .get("/forum/")
        .then((res) => res.data)
        .then((data) => setQuestions(data))
        .catch((err) => alert(err));
    } else {
      api
        .post("/forum/", { query: query })
        .then((res) => res.data)
        .then((data) => setQuestions(data))
        .catch((err) => alert(err));
    }
    setIsLoading(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem(QUERY, query);
    getQuestions();
  }

  return(
    <div>
    {questions.map((question) => {
      <QuestionItem question={question} key={question.id}/>
    })}
    <form onSubmit={handleSubmit}>
    <h1>Search for already asked Questions</h1>
    <input
      className="form-input"
      type="text"
      value={query}
      onChange={(e) => {
        setQuery(e.target.value);
      }}
      placeholder="Have any doubts? Ask them here!"
    />
    {isLoading && <LoadingIndicator />}
    <button type="submit">Go</button>
    </form>
    </div>
  );
}

export default Forum;
