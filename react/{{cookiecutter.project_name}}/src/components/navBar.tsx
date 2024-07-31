const NavBar = () => {

    return (
        <>
            <div className="flex flex-row px-[3vh] sm:px-[9rem] h-[50px] py-8 items-center justify-center text-white bg-emerald-600 " id="navBar">
                <a href="/" className="h-full flex items-center aspect-square">
                    Logo
                </a>
                <div className="flex-grow"/>
                <div className="flex-row gap-10 h-10 hidden sm:flex items-center">

                    {/*<button>Make NaveBar Buttons</button>*/}

                </div>


            </div>
        </>
    );
}

export default NavBar
