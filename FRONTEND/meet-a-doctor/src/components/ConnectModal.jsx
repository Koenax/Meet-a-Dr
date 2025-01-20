
const ConnectModal = ({ doctor, onClose }) => {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
              <h2 className="text-xl font-bond mb-4">Connect with {doctor}</h2>
              <div className="flex flex-col gap-4">
                  <button className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
                      Start Audio Call
                  </button>
                  <button className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
                      Start Video Call
                  </button>
                  <button className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
                      Start Chat
                  </button>
              </div>
              <button 
              className="mt-4 text-grey-600 underline" 
              onClick={onClose}
              >
                  Cancel
              </button>
          </div>
      </div>
    );
  };
  
  export default ConnectModal;