import { twitter, discord, instagram, facebook, telegram } from "../assets";
import face from "../assets/face.webp";
import chat from "../assets/chat.webp";
import call from "../assets/call.webp";
import news from "../assets/news.webp";

export const features = [
  {
    id: "feature-0",
    title: "Make a Video Call",
    description: `
      Dialer Video connects you to your patient through a no-reply
      text message. Your cell number is kept private — you
      designate the callback number. And it works with any
      smartphone. Your patient does not need to download an app
      or create an account. With a simple tap, you’re practicing
      telemedicine.
    `,
    image: face,
    altText: "face",
  },
  {
    id: "feature-1",
    title: "Make a Voice Call",
    description: `
      Use your cell phone to call patients without revealing your private number.
      When their phone rings, patients see your office number (or any number you designate) on their CallerID. Or, 
      skip the ring and go straight to voicemail for non-urgent updates. Free, HIPAA compliant and easy to use.
    `,
    image: call,
    altText: "voice call",
  },
  {
    id: "feature-2",
    title: "Send a Simple chart Note",
    description: `
      Breeze through admin chores like insurance paperwork,
      progress notes, and even grant proposal drafts.
    `,
    image: chat,
    altText: "chart note",
  },
  {
    id: "feature-3",
    title: "Read Medical News",
    description: `
      Essential news and research publications — chosen for you
      from hundreds of thousands of articles per week.
    `,
    image: news,
    altText: "medical news",
  },
];

export const navItems = [
  { label: "Features", href: "#" },
  { label: "Individuals", href: "#" },
  { label: "Pricing", href: "#" },
  { label: "Testimonials", href: "#" },
  { label: "Contact", href: "#" }
];

export const socials = [
{
  id: "0",
  title: "Discord",
  iconUrl: discord,
  url: "#",
},
{
  id: "1",
  title: "Twitter",
  iconUrl: twitter,
  url: "#",
},
{
  id: "2",
  title: "Instagram",
  iconUrl: instagram,
  url: "#",
},
{
  id: "3",
  title: "Telegram",
  iconUrl: telegram,
  url: "#",
},
{
  id: "4",
  title: "Facebook",
  iconUrl: facebook,
  url: "#",
},
];