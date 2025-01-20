import useAuth from "../components/UseAuth";
import Sidebar from "../components/Sidebar";
import NavbarPatient from "../components/NavbarPatients";

const DoctorDashboard = () => {
  useAuth("doctor");

  return (
    <div className="h-screen flex flex-col">
      <NavbarPatient />
      <div className="flex flex-grow">
        <Sidebar role="doctor" />
        <main className="flex flex-grow bg-grey-100 p-6 w-full">
          <h1 className="text-2xl font-bold">Welcome to the Doctor Dashboard</h1>
          {/* Add dashboard features here */}
        </main>
      </div>
    </div>
  );
};

export default DoctorDashboard;
