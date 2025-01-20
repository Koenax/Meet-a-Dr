import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import Description from "./components/Description";
import Feature from "./components/Feature";
import Footer from "./components/Footer";
import Registrations from "./pages/Registrations";
import SignIn from "./pages/SignIn";
import PatientDashboard from "./pages/PatientDashboard";
import DoctorDashboard from "./pages/DoctorDashboard";
import DoctorProfile from "./pages/DoctorProfile";

const App = () => {
  return (
    <Router>
      <main className="sticky top-0 z-50py-0 backdrop-blur-lg bg-black">
        <div className="max-w-screen-xl mx-auto px-4 sm:px-6 lg:px-8 ">
          <Routes>
            {/* Route for the Home Page */}
            <Route
              path="/"
              element={
                <>
                  <Navbar />
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
            <Route path="/patient-dashboard" element={<PatientDashboard />} />
            <Route path="/doctor-dashboard" element={<DoctorDashboard />} />
            <Route path="/doctor-profile" element={<DoctorProfile />} />

          </Routes>
        </div>
        <Footer />
      </main>
    </Router>
  );
};

export default App;