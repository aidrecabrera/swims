import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { Link } from "@tanstack/react-router";

export function Component() {
  return (
    <div className="flex flex-col min-h-[100dvh]">
      <header className="flex items-center px-4 lg:px-6 h-14">
        <Link className="flex items-center justify-center" href="#">
          <DropletsIcon className="w-6 h-6" />
          <span className="text-lg font-semibold">SWIMS</span>
        </Link>
        <nav className="flex gap-4 ml-auto sm:gap-6">
          <Link
            className="text-sm font-medium hover:underline underline-offset-4"
            href="#"
          >
            Login
          </Link>
          <Link
            className="text-sm font-medium hover:underline underline-offset-4"
            href="#"
          >
            Register
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  Sustainable Water Inspection Monitoring System
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  SWIMS is a cutting-edge solution that revolutionizes water
                  quality monitoring and management. With advanced sensors and
                  real-time data analysis, SWIMS ensures the sustainability and
                  safety of your water resources.
                </p>
              </div>
              <div className="space-x-4">
                <Link
                  className="inline-flex items-center justify-center px-4 py-2 text-sm font-medium transition-colors bg-gray-900 rounded-md shadow h-9 text-gray-50 hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                  href="#"
                >
                  Get Started
                </Link>
                <Link
                  className="inline-flex items-center justify-center px-4 py-2 text-sm font-medium transition-colors bg-white border border-gray-200 rounded-md shadow-sm h-9 hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                  href="#"
                >
                  Learn More
                </Link>
              </div>
            </div>
          </div>
        </section>
        <section
          className="w-full py-12 bg-gray-100 md:py-24 lg:py-32 dark:bg-gray-800"
          id="features"
        >
          <div className="container px-4 md:px-6">
            <div className="grid items-center gap-6 lg:grid-cols-[1fr_500px] lg:gap-12 xl:grid-cols-[1fr_550px]">
              <div className="flex flex-col justify-center space-y-4">
                <div className="space-y-2">
                  <div className="inline-block px-3 py-1 text-sm bg-gray-100 rounded-lg dark:bg-gray-800">
                    Key Features
                  </div>
                  <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                    Revolutionize Water Monitoring
                  </h2>
                  <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                    SWIMS combines advanced sensors, real-time data analysis,
                    and intuitive reporting to provide a comprehensive solution
                    for sustainable water management.
                  </p>
                </div>
                <ul className="grid gap-4">
                  <li className="flex items-start gap-2">
                    <CheckIcon className="flex-shrink-0 w-5 h-5 mt-1 text-gray-500 dark:text-gray-400" />
                    <div>
                      <h3 className="text-lg font-medium">
                        Real-Time Monitoring
                      </h3>
                      <p className="text-gray-500 dark:text-gray-400">
                        SWIMS continuously monitors water quality parameters,
                        providing instant alerts and insights.
                      </p>
                    </div>
                  </li>
                  <li className="flex items-start gap-2">
                    <CheckIcon className="flex-shrink-0 w-5 h-5 mt-1 text-gray-500 dark:text-gray-400" />
                    <div>
                      <h3 className="text-lg font-medium">
                        Predictive Analytics
                      </h3>
                      <p className="text-gray-500 dark:text-gray-400">
                        Advanced algorithms forecast water quality trends and
                        potential issues, enabling proactive management.
                      </p>
                    </div>
                  </li>
                  <li className="flex items-start gap-2">
                    <CheckIcon className="flex-shrink-0 w-5 h-5 mt-1 text-gray-500 dark:text-gray-400" />
                    <div>
                      <h3 className="text-lg font-medium">
                        Comprehensive Reporting
                      </h3>
                      <p className="text-gray-500 dark:text-gray-400">
                        Detailed reports and dashboards provide insights to
                        optimize water usage and ensure compliance.
                      </p>
                    </div>
                  </li>
                </ul>
              </div>
              <img
                alt="SWIMS Features"
                className="object-cover object-center mx-auto overflow-hidden aspect-video rounded-xl sm:w-full lg:order-last"
                height="310"
                src="/placeholder.svg"
                width="550"
              />
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="grid items-center gap-6 lg:grid-cols-[500px_1fr] lg:gap-12 xl:grid-cols-[550px_1fr]">
              <img
                alt="About SWIMS"
                className="object-cover object-center mx-auto overflow-hidden aspect-video rounded-xl sm:w-full"
                height="310"
                src="/placeholder.svg"
                width="550"
              />
              <div className="flex flex-col justify-center space-y-4">
                <div className="space-y-2">
                  <div className="inline-block px-3 py-1 text-sm bg-gray-100 rounded-lg dark:bg-gray-800">
                    About SWIMS
                  </div>
                  <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                    Sustainable Water Monitoring for the Future
                  </h2>
                  <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                    SWIMS is a cutting-edge solution that combines advanced
                    sensors, real-time data analysis, and intuitive reporting to
                    revolutionize water quality monitoring and management. Our
                    mission is to ensure the sustainability and safety of water
                    resources for generations to come.
                  </p>
                </div>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Link
                    className="inline-flex items-center justify-center h-10 px-8 text-sm font-medium transition-colors bg-gray-900 rounded-md shadow text-gray-50 hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                    href="#"
                  >
                    Learn More
                  </Link>
                  <Link
                    className="inline-flex items-center justify-center h-10 px-8 text-sm font-medium transition-colors bg-white border border-gray-200 rounded-md shadow-sm hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                    href="#"
                  >
                    Contact Us
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 bg-gray-100 md:py-24 lg:py-32 dark:bg-gray-800">
          <div className="container px-4 md:px-6">
            <div className="grid items-center justify-center gap-4 text-center">
              <div className="space-y-3">
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">
                  Frequently Asked Questions
                </h2>
                <p className="mx-auto max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Get answers to the most common questions about SWIMS.
                </p>
              </div>
              <div className="w-full max-w-2xl mx-auto space-y-4">
                <Collapsible>
                  <CollapsibleTrigger className="flex items-center justify-between w-full px-4 py-3 text-sm font-medium text-left transition-colors bg-white rounded-md hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                    What is SWIMS?
                    <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                  </CollapsibleTrigger>
                  <CollapsibleContent className="px-4 py-3 text-sm text-gray-500 bg-white border border-gray-200 rounded-md shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-gray-400">
                    SWIMS is a comprehensive water quality monitoring and
                    management system that combines advanced sensors, real-time
                    data analysis, and intuitive reporting to ensure the
                    sustainability and safety of water resources.
                  </CollapsibleContent>
                </Collapsible>
                <Collapsible>
                  <CollapsibleTrigger className="flex items-center justify-between w-full px-4 py-3 text-sm font-medium text-left transition-colors bg-white rounded-md hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                    How does SWIMS work?
                    <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                  </CollapsibleTrigger>
                  <CollapsibleContent className="px-4 py-3 text-sm text-gray-500 bg-white border border-gray-200 rounded-md shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-gray-400">
                    SWIMS uses a network of advanced sensors to continuously
                    monitor water quality parameters, such as pH, turbidity,
                    dissolved oxygen, and more. The data is then analyzed in
                    real-time, and the system provides instant alerts and
                    insights to help you manage your water resources
                    effectively.
                  </CollapsibleContent>
                </Collapsible>
                <Collapsible>
                  <CollapsibleTrigger className="flex items-center justify-between w-full px-4 py-3 text-sm font-medium text-left transition-colors bg-white rounded-md hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                    What are the key features of SWIMS?
                    <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                  </CollapsibleTrigger>
                  <CollapsibleContent className="px-4 py-3 text-sm text-gray-500 bg-white border border-gray-200 rounded-md shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-gray-400">
                    SWIMS key features include real-time monitoring, predictive
                    analytics, comprehensive reporting, and intuitive
                    dashboards. The system is designed to provide actionable
                    insights and enable proactive water management.
                  </CollapsibleContent>
                </Collapsible>
                <Collapsible>
                  <CollapsibleTrigger className="flex items-center justify-between w-full px-4 py-3 text-sm font-medium text-left transition-colors bg-white rounded-md hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                    How can I get started with SWIMS?
                    <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                  </CollapsibleTrigger>
                  <CollapsibleContent className="px-4 py-3 text-sm text-gray-500 bg-white border border-gray-200 rounded-md shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-gray-400">
                    To get started with SWIMS, you can sign up for a free trial
                    on our website. Our team will work with you to understand
                    your specific water monitoring needs and provide a
                    customized solution. We offer flexible pricing plans and
                    comprehensive support to ensure a seamless implementation.
                  </CollapsibleContent>
                </Collapsible>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

function CheckIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M20 6 9 17l-5-5" />
    </svg>
  );
}

function ChevronDownIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m6 9 6 6 6-6" />
    </svg>
  );
}

function DropletsIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z" />
      <path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97" />
    </svg>
  );
}
