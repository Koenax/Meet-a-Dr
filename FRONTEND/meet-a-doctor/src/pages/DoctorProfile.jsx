import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import axiosInstance from "../api/axiosInstance";


const DoctorProfile = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    practice_name: "",
    bio: "",
    services_offered: "",
    category: "",
    consultation_fee: "",
    city: "",
    town: "",
    province: "",
    image: null,
  });

  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState("");

  // Define handleChange here
  const handleChange = (e) => {
    if (e.target.name === "image") {
      setFormData({ ...formData, [e.target.name]: e.target.files[0] });
    } else {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    }
  };

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axiosInstance.get("/api/doctors/profile/");
        if (response.data) {
          setFormData({
            practice_name: response.data.practice_name || "",
            bio: response.data.bio || "",
            services_offered: response.data.services_offered || "",
            category: response.data.category || "",
            consultation_fee: response.data.consultation_fee || "",
            city: response.data.city || "",
            town: response.data.town || "",
            province: response.data.province || "",
            image: null,
          });
          setIsEditing(true);
        }
      } catch (err) {
        console.error("Error fetching profile:", err);
      }
    };

    fetchProfile();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.practice_name || !formData.bio || !formData.city || (!formData.image && !isEditing)) {
      setError("Please fill in all required fields.");
      return;
    }

    const formDataToSend = new FormData();
    Object.keys(formData).forEach((key) => {
      if (formData[key]) {
        formDataToSend.append(key, formData[key]);
      }
    });

    try {
      if (isEditing) {
        // await axiosInstance.put("/api/doctors/profile/", formDataToSend, {
          // headers: {
            // "Content-Type": "multipart/form-data",
          // },
        // });
      } else {
        await axiosInstance.post("/api/doctors/create/", formDataToSend, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
      }
      navigate("/doctor-dashboard");
    } catch (err) {
      setError("Error submitting the form. Please try again.");
      console.error(err);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-3 p-8 bg-white shadow-lg rounded-lg border">
      <h1 className="text-3xl font-bold text-gray-800 mb-6 text-center">
        {isEditing ? "Edit Your Doctor Profile" : "Create Your Doctor Profile"}
      </h1>
      {error && <div className="text-red-600 mb-4">{error}</div>}
      <form onSubmit={handleSubmit}>
        {/* Fields */}
        <div className="mb-4">
          <label htmlFor="practice_name" className="block text-sm font-medium text-gray-700 mb-2">
            Practice Name
          </label>
          <input
            type="text"
            name="practice_name"
            value={formData.practice_name}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
          <label htmlFor="bio" className="block text-sm font-medium text-gray-700 mb-2">
            Bio
          </label>
          <input
            type="text"
            name="bio"
            value={formData.bio}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
          <label htmlFor="city" className="block text-sm font-medium text-gray-700 mb-2">
            City
          </label>
          <input
            type="text"
            name="city"
            value={formData.city}
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        {/* Other input fields remain the same */}
        <div className="mb-4">
          <label htmlFor="image" className="block text-sm font-medium text-gray-700 mb-2">
            Profile Image
          </label>
          <input
            type="file"
            name="image"
            onChange={handleChange}
            className="w-full border px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            required={!isEditing}
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
        >
          {isEditing ? "Update Profile" : "Save Profile"}
        </button>
      </form>
    </div>
  );
};

export default DoctorProfile;
