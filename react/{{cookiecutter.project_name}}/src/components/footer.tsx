import {BsGithub, BsLinkedin} from "react-icons/bs";
import {Divider} from "@mantine/core";

const Footer = () => {
    return (
        <footer className="w-screen bg-black flex flex-col px-[3vh] sm:px-[9rem] pb-[2vh] sm:pb-5 pt-[2vh] sm:pt-10 text-[#e1e1e1] text-sm select-none font-light z-0">

            <div className="flex flex-row justify-between font-normal pb-2">
                <div className="text-2xl flex flex-col gap-2">
                    <div>
                        {/*  Company name or logo  */}
                    </div>
                    <div className="flex flex-row gap-5">
                        <a href={import.meta.env.VITE_COMPANY_LINKEDIN_URL}>
                            <BsLinkedin size={20} />
                        </a>
                        <a href={import.meta.env.VITE_COMPANY_GITHUB_URL}>
                            <BsGithub size={20}/>
                        </a>
                    </div>
                </div>

                <div className="flex flex-col gap-2 sm:gap-3 pt-2">
                    {/*    Some footer links */}
                </div>
            </div>

            <div className="">
                <div className="flex flex-col gap-5">
                    <div>
                        {/*©Insert company name  Ltd. All rights reserved.*/}
                    </div>
                    <div>{/* This is a great place to put company registration details*/}<br/>
                        {/* This is a great place to put company registration details*/}
                    </div>
                </div>
            </div>
            <div className="mt-5 flex justify-center">
                <div className="w-1/3">
                    <Divider className="opacity-60" />

                </div>
            </div>

        </footer>
    )
}
export default Footer;
