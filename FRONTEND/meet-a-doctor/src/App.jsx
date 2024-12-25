import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import Description from "./components/Description";
import Body from "./components/Body";

const App = () => {
  return (
    <>
    <Navbar />
    <div className="max-w-7xl mx-auto pt-5 px-5f">
      <HeroSection />
      <Description />
      <Body />
    </div>
    </>
  );
};

export default App;
