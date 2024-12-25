import hero2 from "../assets/hero2.jpeg";

const HeroSection = () => {
  return (
    <div
      className="bg-cover bg-center text-white py-16 px-4"
      style={{
        backgroundImage: `url(${hero2})`,
      }}
    >
      <div className="flex flex-col items-center mt-6 lg:mt-20 bg-black bg-opacity-50 p-8 rounded-lg">
        <h1 className="text-4xl sm:text-6xl lg:text-7xl text-center tracking-wide">
          Healthcare with a
          <span className="bg-gradient-to-r from-orange-500 to-red-800 text-transparent bg-clip-text">
            {" "}
            Modern Touch
          </span>
        </h1>
        <p className="text-center mt-4 max-w-2xl">
          Our telehealth solutions make it easy for people to access best-in-class care whenever and wherever, while driving down overall healthcare costs.
        </p>
        <div className="flex justify-center my-10">
          <a
            href="#"
            className="bg-gradient-to-r from-orange-500 to-orange-800 py-3 px-4 mx-3 rounded-md text-white"
          >
            For Organisation
          </a>
          <a
            href="#"
            className="bg-gradient-to-r from-orange-500 to-orange-800 py-3 px-4 mx-3 rounded-md text-white"
          >
            For Patient
          </a>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;

