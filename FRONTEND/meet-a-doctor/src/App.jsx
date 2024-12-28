import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import Description from "./components/Description";
import Feature from "./components/Feature";
import Footer from "./components/Footer";
import Registrations from "./pages/Registrations";
import SignIn from "./pages/SignIn";

const App = () => {
  return (
    <Router>
      <Navbar />
      <main className="overflow-hidden bg-black">
        <div className="max-w-screen-xl mx-auto px-4 sm:px-6 lg:px-8">
          <Routes>
            {/* Route for the Home Page */}
            <Route
              path="/"
              element={
                <>
                  <HeroSection />
                  <Description />
                  <Feature />
                </>
              }
            />

            {/* Route for the Registration Page */}
            <Route path="/register" element={<Registrations />} />

            {/* Route for the Sign-In Page */}
            <Route path="/signin" element={<SignIn />} />
          </Routes>
        </div>
      </main>
      <Footer />
    </Router>
  );
};

export default App;