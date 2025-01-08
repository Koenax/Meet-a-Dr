import { socials } from "../constants";

function Footer() {
  return (
    <div className="container flex sm:justify-between justify-center gap-10 max-sm:flex-col bg-black">
        <p className="caption text-n-4 lg:block text-white pt-2">
        © {new Date().getFullYear()}. All rights reserved.
        </p>

        <ul className="flex gap-5 flex-wrap">
            {socials.map((item) => (
                <a
                key={item.id}
                href={item.url}
                target="_blank"
                className="flex item-center justify-center w-10 h-10 bg-n-7 rounded-full transition-colors hover:bg-n-6"
                >
                    <img src={item.iconUrl} width={16} height={16} alt={item.title} />
                </a>
            ))}
        </ul>
    </div>
  );
};

export default Footer;