import {
  BrowserRouter as Router,
  Routes,
  Route,
  BrowserRouter
} from "react-router-dom";

import './App.css';
import Header from './components/Header'
import ModulesListPage from './pages/ModulesListPage'
import ModulePage from "./pages/ModulePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ModulesListPage/>} />
        <Route path="/module/:id" element={<ModulePage/>} />
      </Routes>
    </Router>
  );
}

export default App;
