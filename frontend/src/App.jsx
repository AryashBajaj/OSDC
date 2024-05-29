import react from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import api from "./api";
import Login from "./pages/Login";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoutes";
import Question from "./pages/Question";
import Forum from "./pages/Forum";
import Server from "./pages/Server";
import Channel from "./pages/Channel";

function Logout() {
  localStorage.clear();
  return <Navigate to="/login"></Navigate>;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register></Register>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home></Home>
            </ProtectedRoute>
          }
        />
        <Route path="/login/" element={<Login></Login>} />
        <Route path="/logout/" element={<Logout></Logout>} />
        <Route
          path="/register/"
          element={<RegisterAndLogout></RegisterAndLogout>}
        />
        <Route
          path="/Forum/"
          element={<Forum></Forum>}
        />
        <Route
          path="/Forum/:qid/"
          element={<Question></Question>}
        />
        <Route 
          path="/Server/:sid/channel/"
          element={<Server></Server>}
        />
        <Route 
          path="Server/channel/:cid/"
          element={<Channel></Channel>}
        />
        <Route path="*" element={<NotFound></NotFound>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
