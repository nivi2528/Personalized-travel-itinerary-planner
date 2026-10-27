import { Link, Route, Routes } from "react-router-dom";
import Login from "./pages/Login.jsx";
import Preferences from "./pages/Preferences.jsx";
import Itinerary from "./pages/Itinerary.jsx";
import SavedItineraries from "./pages/SavedItineraries.jsx";

function App() {
  return (
    <div className="app">
      <header>
        <h1>Personalized Travel Itinerary Planner</h1>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/login">Login</Link>
          <Link to="/preferences">Preferences</Link>
          <Link to="/itinerary">Itinerary</Link>
          <Link to="/saved">Saved</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route
            path="/"
            element={
              <p>
                Collect preferences, generate a day-by-day trip plan, then save,
                edit, or regenerate it. Backend and AI are not connected yet.
              </p>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/preferences" element={<Preferences />} />
          <Route path="/itinerary" element={<Itinerary />} />
          <Route path="/saved" element={<SavedItineraries />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
