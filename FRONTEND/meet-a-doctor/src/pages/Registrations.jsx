import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../api/axiosInstance";

const Registration = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
    password2: "",
  });

  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.email || !formData.password1 || !formData.password2) {
      setError("Please fill in all required fields.");
      return;
    }

    try {
      const response = await axiosInstance.post("/api/auth/register/", formData);

      alert("Registration successful! Please sign in.");
      navigate("/signin");
    } catch (err) {
      setError(err.response?.data?.message || "Registration failed. Please try again.");
      console.error("Registration Error:", err);
    }

  };

  return (
    <div className="max-w-lg mx-auto mt-3 p-8 bg-white shadow-lg rounded-lg border">
      <h1 className="text-3xl font-bold text-gray-800 mb-6 text-center">Register an Account</h1>
      {error && <div className="text-red-600 mb-4">{error}</div>}
      <form onSubmit={handleSubmit}>
      <div className="mb-4">
          <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password1" className="block text-sm font-medium text-gray-700 mb-2">Password1</label>
          <input
            type="password"
            name="password1"
            value={formData.password1}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password2" className="block text-sm font-medium text-gray-700 mb-2">Password2</label>
          <input
            type="password"
            name="password2"
            value={formData.password2}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default Registration;
