import { Menu, X } from "lucide-react";
import { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import logo from "../assets/logo.png";
import { navItems } from "../constants";

const Navbar = () => {
  const navigate = useNavigate();
  const [mobileDrawerOpen, setMobileDrawerOpen] = useState(false);

  const toggleNavbar = () => {
    setMobileDrawerOpen(!mobileDrawerOpen);
  };

  return (
    <nav className="sticky top-0 z-50 py-3 backdrop-blur-lg border-b border-neutral-700/80 bg-gray-400">
      <div className="container px-4 mx-auto relative">
        {/* Logo and Toggle Button */}
        <div className="flex justify-between items-center">
          <div
            className="flex items-center flex-shrink-0 cursor-pointer"
            onClick={() => navigate("/")}
          >
            <img className="h-10 w-10 mr-2" src={logo} alt="Logo" />
            <span className="text-xl tracking-tight text-white">Meet-a-Doctor</span>
          </div>
          {/* Desktop Navigation */}
          <ul className="hidden lg:flex ml-14 space-x-12">
            {navItems.map((item, index) => (
              <li key={index}>
                <NavLink
                  to={item.href}
                  className={({ isActive }) =>
                    `text-lg text-white hover:text-orange-500 transition-colors ${
                      isActive ? "text-orange-500" : ""
                    }`
                  }
                >
                  {item.label}
                </NavLink>
              </li>
            ))}
          </ul>
          {/* Desktop Buttons */}
          <div className="hidden lg:flex justify-center space-x-4 items-center">
            <NavLink
              to="/signin"
              className="py-2 px-3 border rounded-md text-white hover:bg-neutral-800 transition-colors"
            >
              Sign In
            </NavLink>
            <NavLink
              to="/register"
              className="bg-gradient-to-r from-orange-500 to-orange-800 py-2 px-3 rounded-md text-white hover:opacity-90 transition-opacity"
            >
              Create an account
            </NavLink>
          </div>
          {/* Mobile Menu Toggle */}
          <button
            onClick={toggleNavbar}
            aria-label="Toggle navigation menu"
            className="lg:hidden focus:outline-none"
          >
            {mobileDrawerOpen ? <X /> : <Menu />}
          </button>
        </div>

        {/* Mobile Drawer */}
        {mobileDrawerOpen && (
          <div className="fixed inset-0 z-20 bg-neutral-900 w-full h-screen p-6 flex flex-col items-center">
            {/* Collapse Button */}
            <button
              onClick={toggleNavbar}
              aria-label="Close menu"
              className="absolute top-6 right-6 text-white focus:outline-none"
            >
              <X size={24} />
            </button>
            {/* Navigation Links */}
            <ul className="space-y-4 text-center mt-12">
              {navItems.map((item, index) => (
                <li key={index}>
                  <NavLink
                    to={item.href}
                    className={({ isActive }) =>
                      `text-lg text-white hover:text-orange-500 transition-colors ${
                        isActive ? "text-orange-500" : ""
                      }`
                    }
                  >
                    {item.label}
                  </NavLink>
                </li>
              ))}
            </ul>
            {/* Mobile Buttons */}
            <div className="flex flex-col space-y-4 mt-6">
              <NavLink
                to="/signin"
                className="py-2 px-3 border rounded-md text-white text-center hover:bg-neutral-800 transition-colors"
              >
                Sign In
              </NavLink>
              <NavLink
                to="/register"
                className="py-2 px-3 rounded-md text-white text-center bg-gradient-to-r from-orange-500 to-orange-800 hover:opacity-90 transition-opacity"
              >
                Create an account
              </NavLink>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
