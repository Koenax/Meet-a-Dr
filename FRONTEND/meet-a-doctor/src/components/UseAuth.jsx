import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

const useAuth = (role) => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user"));

  useEffect(() => {
    if (!user || user.role !== role) {
      alert("Access denied. Please log in as a doctor.");
      navigate("/signin");
    }
  }, [user, role, navigate]);

  return user;
};

export default useAuth;
