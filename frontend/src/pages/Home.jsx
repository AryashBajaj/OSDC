import { react, useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { QUERY } from "../constants";
import api from "../api";
import LoadingIndicator from "../components/LoadingIndicator";

function Home() {
  console.log("Home");
  const [isLoading, setIsLoading] = useState(false);
  const [servers, setServers] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    getServers();
  }, []);

  console.log(servers);

  const navigate = useNavigate();

  const getServers = () => {
    setIsLoading(true);
    api
      .get("server/")
      .then((res) => res.data)
      .then((data) => setServers(data))
      .catch((err) => alert(err));
    setIsLoading(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem(QUERY, query);
    navigate("/Forum/")
  }

  <form onSubmit={handleSubmit}>
    <h1>Search for already asked Questions</h1>
        <input 
            className="form-input"
            type="text"
            value={query}
            onChange={(e) => {setQuery(e.target.value);}}
            placeholder="Have any doubts? Ask them here!"
        />
        { isLoading && <LoadingIndicator />}
        <button type="submit">Go</button>
  </form>

}

export default Home;
