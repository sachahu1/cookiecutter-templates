import NavBar from "../components/navBar.tsx";

import Footer from "../components/footer.tsx";
import BaseView from "./views/baseView.tsx";

const FrontPage = () => {


  return (
    <div className="relative min-h-[100vh] font-rubik tracking-wide">
      <div
        className="w-screen z-40 select-none ">
        <NavBar/>
      </div>

      <BaseView/>

      <Footer/>
    </div>

  );

};

export default FrontPage;
