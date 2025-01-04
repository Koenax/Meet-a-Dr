import { Search } from "lucide-react";
import logo from "../assets/logo.png";
const NavbarPatient = () => {
    return (
        <nav className="sticky top-0 z-50 py-3 backdrop-blur-lg border-b border-neutral-700/800 bg-grey-400">
            <div className="container px-4 mx-auto flex justify-between items-center">
                <div className="flex items-center">
                    <img className="h-10 w-10 mr-2" src={logo} alt="Logo" />
                    <span className="text-xl font-bond text-white">Meet-a-Doctor</span>
                </div>
                <div className="relative">
                    <input
                    type="text"
                    placeholder="Meet a doctor..."
                    className="px-4 py-2 rounded-md border border-neutral-700 bg-white focus:outline-none"
                     />
                    <Search className="absolute top-2.5 right-3 text-grey-500" />
                </div>
            </div>
        </nav>
    );
};

export default NavbarPatient;