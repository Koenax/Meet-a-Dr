import { NavLink } from "react-router-dom";
import { User, Settings, Clock, CalendarDays } from "lucide-react";

const Sidebar = ({ role }) => {
  const menuItems = role === "doctor" 
    ? [
        { icon: <User />, label: "Profile", path: "/doctor-profile" },
        { icon: <CalendarDays />, label: "Schedules", path: "/doctor-schedules" },
        { icon: <Settings />, label: "Settings", path: "/doctor-settings" },
        { icon: <Clock />, label: "History", path: "/doctor-history" },
      ]
    : [
        { icon: <User />, label: "Profile", path: "/patient-profile" },
        { icon: <CalendarDays />, label: "Appointments", path: "/patient-appointments" },
        { icon: <Settings />, label: " Settings", path: "/patient-settings" },
        { icon: <Clock />, label: "Activity Log", path: "/patient-activity-log" },
      ];

  return (
    <aside className="w-1/4 h-full bg-neutral-800 text-white p-4 space-y-6">
      <ul className="space-y-4">
        {menuItems.map((item, index) => (
          <li key={index}>
            <NavLink
              to={item.path}
              className={({ isActive }) =>
                `flex items-center space-x-3 cursor-pointer p-2 rounded-md ${
                  isActive ? "bg-blue-600" : "hover:bg-neutral-700"
                }`
              }
            >
              {item.icon}
              <span>{item.label}</span>
            </NavLink>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default Sidebar;
