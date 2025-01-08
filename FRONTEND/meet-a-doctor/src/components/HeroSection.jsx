import hero2 from "../assets/hero2.jpeg";

const HeroSection = () => {
  return (
    <div className="relative h-screen overflow-hidden rounded-b-[0.9rem] pt-5">
      {/* Background Image */}
      <img
        src={hero2}
        className="absolute inset-0 w-full h-full object-cover"
        alt="doc and patient"
      />
      {/* Overlay with Content */}
      <div className="absolute inset-0 bg-black bg-opacity-40 flex flex-col items-center justify-center text-white">
        {/* Main Heading */}
        <h1 className="text-3xl sm:text-5xl lg:text-6xl text-center tracking-wide">
          Healthcare with a
          <span className="bg-gradient-to-r from-orange-500 to-red-800 text-transparent bg-clip-text">
            {" "}
            Modern Touch
          </span>
        </h1>

        {/* Subheading */}
        <p className="text-center mt-4 max-w-2xl text-sm sm:text-base lg:text-lg">
          Our telehealth solutions make it easy for people to access best-in-class care
          whenever and wherever, while driving down overall healthcare costs.
        </p>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row justify-center my-6 space-y-4 sm:space-y-0 sm:space-x-4">
          <a
            href="#"
            className="bg-gradient-to-r from-orange-500 to-orange-800 py-3 px-6 rounded-md text-white text-center hover:opacity-90 transition-opacity"
          >
            For Organisation
          </a>
          <a
            href="#"
            className="bg-gradient-to-r from-orange-500 to-orange-800 py-3 px-6 rounded-md text-white text-center hover:opacity-90 transition-opacity"
          >
            For Patient
          </a>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
