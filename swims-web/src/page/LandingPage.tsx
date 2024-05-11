import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible"
import { Link } from "@tanstack/react-router"

export default function LandingPage() {
    return (
        <div className="flex flex-col min-h-[100dvh]">
            <header className="px-4 mt-2 lg:px-6 h-14 flex items-center container">
                <Link className="flex items-center justify-center gap-2 mt-2" href="#">
                    <DropletsIcon className="h-10 w-10" />
                    <span className="font-bold text-lg">SWIMS</span>
                </Link>
                <nav className="ml-auto flex gap-2 sm:gap-2 z-50">
                    <Link to="/login" className="text-sm font-medium hover:underline underline-offset-4" href="#">
                        Login
                    </Link>
                    <Link to="/register" className="text-sm font-medium hover:underline underline-offset-4" href="#">
                        Register
                    </Link>
                </nav>
            </header>
            <main className="flex-1">
                <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 flex flex-row items-center justify-centerq">
                    <div className="container px-4 md:px-6">
                        <div className="flex flex-col items-center space-y-4 text-center">
                            <div className="space-y-2">
                                <h1 className="text-3xl max-w-5xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                                    Sustainable Water Inspection and Monitoring System. Pioneers solutions for aquaculture's evolutions.
                                </h1>
                            </div>
                            <div className="space-x-2">
                                <Link
                                    className="inline-flex h-9 items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-primary dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                                    to="/login"
                                >
                                    Get Started
                                </Link>
                                <Link
                                    className="inline-flex h-9 items-center justify-center rounded-md border border-gray-200 bg-white px-4 py-2 text-sm font-medium shadow-sm transition-colors hover:bg-background hover:text-primary focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                                    href="#"
                                >
                                    Learn More
                                </Link>
                            </div>
                        </div>
                    </div>
                </section>
                <section className="w-full py-12 md:py-24 lg:py-32 bg-background dark:bg-gray-800" id="features">
                    <div className="container px-4 md:px-6">
                        <div className="grid items-center gap-6 lg:grid-cols-[1fr_500px] lg:gap-12 xl:grid-cols-[1fr_550px]">
                            <div className="flex flex-col justify-center space-y-4">
                                <div className="space-y-2">
                                    <div className="inline-block rounded-lg bg-background px-1 py-1 text-sm dark:bg-gray-800">
                                        Key Features
                                    </div>
                                    <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Revolutionize Water Monitoring</h2>
                                    <p className="max-w-[600px] text-text md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-primary-foreground">
                                        SWIMS combines advanced sensors, real-time data analysis, and intuitive reporting to provide a
                                        comprehensive solution for sustainable water management.
                                    </p>
                                </div>
                                <ul className="grid gap-4">
                                    <li className="flex items-start gap-2">
                                        <CheckIcon className="mt-1 h-5 w-5 flex-shrink-0 text-text dark:text-primary-foreground" />
                                        <div>
                                            <h3 className="text-lg font-medium">Real-Time Monitoring</h3>
                                            <p className="text-text dark:text-primary-foreground">
                                                SWIMS continuously monitors water quality parameters, providing instant alerts and insights.
                                            </p>
                                        </div>
                                    </li>
                                    <li className="flex items-start gap-2">
                                        <CheckIcon className="mt-1 h-5 w-5 flex-shrink-0 text-text dark:text-primary-foreground" />
                                        <div>
                                            <h3 className="text-lg font-medium">Predictive Analytics</h3>
                                            <p className="text-text dark:text-primary-foreground">
                                                Advanced algorithms forecast water quality trends and potential issues, enabling proactive
                                                management.
                                            </p>
                                        </div>
                                    </li>
                                    <li className="flex items-start gap-2">
                                        <CheckIcon className="mt-1 h-5 w-5 flex-shrink-0 text-text dark:text-primary-foreground" />
                                        <div>
                                            <h3 className="text-lg font-medium">Comprehensive Reporting</h3>
                                            <p className="text-text dark:text-primary-foreground">
                                                Detailed reports and dashboards provide insights to optimize water usage and ensure compliance.
                                            </p>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                            <img
                                alt="SWIMS Features"
                                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last "
                                height="310"
                                src="https://plus.unsplash.com/premium_photo-1666820202651-314501c88358?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
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
                                className="mx-auto overflow-hidden rounded-xl object-cover object-center sm:w-full h-full"
                                height="310"
                                src="about.png"
                                width="550"
                            />
                            <div className="flex flex-col justify-center space-y-4">
                                <div className="space-y-2">
                                    <div className="inline-block rounded-lg bg-background px-1 py-1 text-sm dark:bg-gray-800">
                                        About SWIMS
                                    </div>
                                    <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                                        Sustainable Water Monitoring
                                    </h2>
                                    <p className="max-w-[600px] text-text md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-primary-foreground">
                                        SWIMS is a solution that combines advanced sensors, real-time data analysis, and
                                        intuitive reporting to revolutionize water quality monitoring and management. Our mission is to
                                        ensure the sustainability and safety of water resources for generations to come.
                                    </p>
                                </div>
                                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                                    <Link
                                        className="inline-flex h-10 items-center justify-center rounded-md bg-primary px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-primary dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                                        href="#"
                                    >
                                        Learn More
                                    </Link>
                                    <Link
                                        className="inline-flex h-10 items-center justify-center rounded-md border border-gray-200 border-gray-200 bg-white px-8 text-sm font-medium shadow-sm transition-colors hover:bg-background hover:text-primary focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                                        href="#"
                                    >
                                        Contact Us
                                    </Link>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <section className="w-full py-12 md:py-24 lg:py-32 bg-background dark:bg-gray-800">
                    <div className="container px-4 md:px-6">
                        <div className="grid items-center justify-center gap-4 text-center">
                            <div className="space-y-3">
                                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Frequently Asked Questions</h2>
                                <p className="mx-auto max-w-[600px] text-text md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-primary-foreground">
                                    Get answers to the most common questions about SWIMS.
                                </p>
                            </div>
                            <div className="mx-auto w-full max-w-2xl space-y-4">
                                <Collapsible>
                                    <CollapsibleTrigger className="flex w-full items-center justify-between rounded-md bg-white px-4 py-3 text-left text-sm font-medium transition-colors hover:bg-background focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                                        What is SWIMS?
                                        <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                                    </CollapsibleTrigger>
                                    <CollapsibleContent className="rounded-md border border-gray-200 bg-white px-4 py-3 text-sm text-text shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-primary-foreground">
                                        SWIMS is a comprehensive water quality monitoring and management system that combines advanced
                                        sensors, real-time data analysis, and intuitive reporting to ensure the sustainability and safety of
                                        water resources.
                                    </CollapsibleContent>
                                </Collapsible>
                                <Collapsible>
                                    <CollapsibleTrigger className="flex w-full items-center justify-between rounded-md bg-white px-4 py-3 text-left text-sm font-medium transition-colors hover:bg-background focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                                        How does SWIMS work?
                                        <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                                    </CollapsibleTrigger>
                                    <CollapsibleContent className="rounded-md border border-gray-200 bg-white px-4 py-3 text-sm text-text shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-primary-foreground">
                                        SWIMS uses a network of advanced sensors to continuously monitor water quality parameters, such as
                                        pH, turbidity, dissolved oxygen, and more. The data is then analyzed in real-time, and the system
                                        provides instant alerts and insights to help you manage your water resources effectively.
                                    </CollapsibleContent>
                                </Collapsible>
                                <Collapsible>
                                    <CollapsibleTrigger className="flex w-full items-center justify-between rounded-md bg-white px-4 py-3 text-left text-sm font-medium transition-colors hover:bg-background focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 dark:bg-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-300">
                                        What are the key features of SWIMS?
                                        <ChevronDownIcon className="h-5 w-5 transition-transform [&[data-state=open]]:rotate-180" />
                                    </CollapsibleTrigger>
                                    <CollapsibleContent className="rounded-md border border-gray-200 bg-white px-4 py-3 text-sm text-text shadow-sm dark:border-gray-800 dark:bg-gray-950 dark:text-primary-foreground">
                                        SWIMS key features include real-time monitoring, predictive analytics, comprehensive reporting, and
                                        intuitive dashboards. The system is designed to provide actionable insights and enable proactive
                                        water management.
                                    </CollapsibleContent>
                                </Collapsible>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    )
}

function CheckIcon(props: any) {
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
    )
}


function ChevronDownIcon(props: any) {
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
    )
}


function DropletsIcon(props: any) {
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
    )
}