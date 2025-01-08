import NavbarPatient from "../components/NavbarPatients";
import Sidebar from "../components/Sidebar";
import doctor_1 from "../assets/doctor_1.jpeg";
import doctor_2 from "../assets/doctor_2.jpeg";
import doctor_3 from "../assets/doctor_3.jpeg";

const PatientDashboard = () => {
  return (
    <div className="h-screen flex flex-col">
      <NavbarPatient />
      <div className="flex flex-grow">
        <Sidebar />
        <main className="flex flex-grow bg-grey-100 p-6 w-full">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {/* Doctor 1 */}
            <div className="bg-white shadow-md rounded-md p-4 flex flex-col items-center transition-transform transform hover:scale-105 hover:shadow-lg">
              <img 
                src={doctor_1}
                alt="Doctor 1" 
                className="w-24 h-24 rounded-full mb-4"
              />
              <h3 className="text-lg font-bold mb-2">Dr. Alice Smith</h3>
              <p className="mb-2">Cardiologist</p>
              <div className="bg-gray-100 p-2 rounded-md mb-4">
                <p className="text-sm">Currently working at: Heart Care Center</p>
                <p className="text-sm">Experience: 10 years</p>
              </div>
              <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mt-auto">
                Connect
              </button>
            </div>

            {/* Doctor 2 */}
            <div className="bg-white shadow-md rounded-md p-4 flex flex-col items-center transition-transform transform hover:scale-105 hover:shadow-lg">
              <img 
                src={doctor_2}
                alt="Doctor 2" 
                className="w-24 h-24 rounded-full mb-4"
              />
              <h3 className="text-lg font-bold mb-2">Dr. John Doe</h3>
              <p className="mb-2">Neurologist</p>
              <div className="bg-gray-100 p-2 rounded-md mb-4">
                <p className="text-sm">Currently working at: NeuroHealth Clinic</p>
                <p className="text-sm">Experience: 8 years</p>
              </div>
              <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mt-auto">
                Connect
              </button>
            </div>

            {/* Doctor 3 */}
            <div className="bg-white shadow-md rounded-md p-4 flex flex-col items-center transition-transform transform hover:scale-105 hover:shadow-lg">
              <img 
                src={doctor_3}
                alt="Doctor 3" 
                className="w-24 h-24 rounded-full mb-4"
              />
              <h3 className="text-lg font-bold mb-2">Dr. Emily Brown</h3>
              <p className="mb-2">Pediatrician</p>
              <div className="bg-gray-100 p-2 rounded-md mb-4">
                <p className="text-sm">Currently working at: Kids Health Hospital</p>
                <p className="text-sm">Experience: 12 years</p>
              </div>
              <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mt-auto">
                Connect
              </button>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default PatientDashboard;
