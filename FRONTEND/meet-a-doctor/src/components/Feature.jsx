import { useState } from "react";
import { features } from "../constants/index";

const Feature = () => {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selectedFeature = features[selectedIndex];

  const handleNext = () => {
    setSelectedIndex((prevIndex) => (prevIndex + 1) % features.length);
  };

  const handlePrevious = () => {
    setSelectedIndex((prevIndex) => (prevIndex - 1 + features.length) % features.length);
  };

  return (
    <div className="relative">
      {/* Navigation Buttons */}
      <button
        className="absolute left-4 top-1/2 transform -translate-y-1/2 bg-gray-200 p-4 rounded-full shadow-md hover:bg-gray-300"
        onClick={handlePrevious}
      >
        <span className="text-xl">&lt;</span>
      </button>
      <button
        className="absolute right-4 top-1/2 transform -translate-y-1/2 bg-gray-200 p-4 rounded-full shadow-md hover:bg-gray-300"
        onClick={handleNext}
      >
        <span className="text-xl">&gt;</span>
      </button>

      {/* Navigation Bar */}
      <nav className="flex justify-around items-center mt-4 py-4">
        {features.map((feature, index) => (
          <button
            key={feature.id}
            className={`px-4 py-2 text-sm font-semibold rounded-md ${
              selectedIndex === index
                ? "bg-gradient-to-r from-orange-500 to-orange-800 text-white"
                : "bg-gray-200"
            }`}
            onClick={() => setSelectedIndex(index)}
          >
            {feature.title}
          </button>
        ))}
      </nav>

      {/* Content Display */}
      <div className="flex flex-col lg:flex-row items-center gap-6 mt-6">
        {/* Image Section */}
        <div className="flex-shrink-0">
          <div className="w-full max-w-xs sm:max-w-md md:max-w-lg">
            <img
              loading="lazy"
              alt={selectedFeature.altText}
              src={selectedFeature.image}
              className="w-full h-auto rounded-md"
            />
          </div>
        </div>

        {/* Write-Up Section */}
        <div className="px-6 sm:px-8 max-w-md sm:self-center">
          <h2 className="text-xl sm:text-2xl lg:text-3xl font-bold text-center lg:text-left">
            {selectedFeature.title}
          </h2>
          <p className="mt-4 text-sm sm:text-base lg:text-lg text-gray-700 text-center lg:text-left">
            {selectedFeature.description}
            <a
              href="#"
              className="text-blue-500 hover:underline focus:underline"
            >
              Learn More
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Feature;
