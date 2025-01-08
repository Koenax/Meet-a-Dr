import { User, Settings, Clock, CalendarDays } from "lucide-react";


const Sidebar = () => {
    const menuItems = [
        { icon: <User />, label: "Profile" },
        {icon: <CalendarDays />, label: "Schedules"},
        { icon: <Settings />, label: "Settings" },
        { icon: <Clock />, label: "History" },
    ];

    return (
        <aside className="w-1/4 h-full bg-neutral-800 text-white p-4 space-y-6">
            <ul className="space-y-4">
                {menuItems.map((item, index) => (
                    <li
                        key={index}
                        className="flex items-center space-x-3 cursor-pointer hover:bg-neutral-700 p-2 rounded-md"
                    >
                        {item.icon}
                        <span>{item.label}</span>
                    </li>
                ))}
            </ul>
        </aside>
    );
};

export default Sidebar;