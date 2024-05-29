import { useState, useEffect } from "react";
import Channel from "./Channel";
import api from "../api";
import { useParams } from "react-router-dom";

function Server() {
  const [details, setDetails] = useState({});
  const [channels, setChannels] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const { sid } = useParams();

  useEffect(() => {
    getChannels();
    getDetails();
  }, []);

  console.log(channels);
  console.log(details);

  const getChannels = () => {
    setIsLoading(true);
    api
      .get(`/server/${sid}/channel/`)
      .then((res) => res.data)
      .then((data) => setChannels(data))
      .catch((err) => alert(err));
    setIsLoading(false);
  };

  const getDetails = () => {
    api
      .get(`/server/servers/${sid}/`)
      .then((res) => res.data)
      .then((data) => setDetails(data))
      .catch((err) => alert(err));
  };
}

export default Server;
