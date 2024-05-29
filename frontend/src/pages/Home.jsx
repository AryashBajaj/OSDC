import { react, useEffect, useState } from "react";
import { Navigate, Router, useNavigate,} from "react-router-dom";
import { QUERY } from "../constants";
import Navbar from "../components/Navbar";
import Texttrans from "../components/Texttrans"
import api from "../api";
import Logo from "../components/Logo"
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

  return(
    <div>
      <Navbar title="Synergy"/>
      <Texttrans/>
      <div className='mb-3 centerForm' style={{
        position: 'absolute',
        top: '600px',
        left: '400px',
        transform: 'translate(-50%, -50%)',
        padding: '8px 12px',
        border: '2px dashed #aaa',
        borderRadius: '6px',
      }}>
        <form>
          <div className="form-group">
            <label htmlFor="exampleFormControlTextarea1"></label>
            <textarea className="form-control" style={{
              width: '300px', // Adjust the width as needed
              height: '70px',
              border: '2px solid #aaa',
              borderRadius: '4px',
              margin: '2px 0',
              outline: 'none',
              padding: '2px',
              boxSizing: 'border-box',
              transition: '0.3s',
              resize: 'none',
              textIndent: '16px',
              lineHeight: '1.6em'
            }} placeholder="What is your question ?" id="exampleFormControlTextarea1" rows="3"></textarea>
          </div>
        </form>
        <Logo/>
      </div>
    </div>
  );

}

export default Home;
