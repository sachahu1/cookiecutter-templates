import {Route, Routes} from "react-router-dom";
import FrontPage from "./pages/FrontPage.tsx";
import {MantineProvider} from "@mantine/core";

function App() {

    return (
        <MantineProvider>

            <div
                className="flex items-center justify-center w-screen h-screen sm:hidden">
                Unfortunately, this website
                is not responsive on mobile at this time. Please visit us from
                your desktop.
            </div>
            <div className="hidden sm:flex">
                <Routes>
                    <Route path="/" element={<FrontPage/>}/>
                </Routes>

            </div>
        </MantineProvider>

    )
}

export default App
