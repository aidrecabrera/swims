import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import {
  createRootRoute,
  Link,
  Outlet,
  useNavigate,
  useRouterState,
} from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";
import { DropletsIcon, Menu } from "lucide-react";

export const Route = createRootRoute({
  component: () => {
    const router = useRouterState();
    const navigate = useNavigate();
    return (
      <>
        {router.location.pathname !== "/" &&
        router.location.pathname !== "/login" &&
        router.location.pathname !== "/register" ? (
          <header className="sticky top-0 z-50 flex items-center h-16 gap-4 px-4 border-b bg-background md:px-6">
            <nav className="flex-col hidden gap-6 text-lg font-medium md:flex md:flex-row md:items-center md:gap-5 md:text-sm lg:gap-6">
              <Link
                href="#"
                className="flex items-center gap-2 text-lg font-semibold md:text-base"
              >
                <DropletsIcon className="w-10 h-10" />
                <span className="sr-only">SWIMS</span>
              </Link>
              <Link
                to="/dashboard"
                className="transition-colors text-foreground hover:text-foreground"
              >
                Dashboard
              </Link>
              <Link
                to="/historical"
                className="transition-colors text-muted-foreground hover:text-foreground"
              >
                Database
              </Link>
            </nav>
            <Sheet>
              <SheetTrigger asChild>
                <Button
                  variant="outline"
                  size="icon"
                  className="shrink-0 md:hidden"
                >
                  <Menu className="w-5 h-5" />
                  <span className="sr-only">Toggle navigation menu</span>
                </Button>
              </SheetTrigger>
              <SheetContent side="left">
                <nav className="grid gap-6 text-lg font-medium">
                  <Link
                    href="#"
                    className="flex items-center gap-2 text-lg font-semibold"
                  >
                    <DropletsIcon className="w-10 h-10" />
                    <span className="sr-only">SWIMS</span>
                  </Link>
                  <Link
                    to="/dashboard"
                    className="transition-colors text-foreground hover:text-foreground"
                  >
                    Dashboard
                  </Link>
                  <Link
                    to="/historical"
                    className="transition-colors text-muted-foreground hover:text-foreground"
                  >
                    Database
                  </Link>
                </nav>
              </SheetContent>
            </Sheet>
            <div className="flex items-center w-full gap-4 md:ml-auto md:gap-2 lg:gap-4">
              <div className="flex-1 ml-auto sm:flex-initial"></div>
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button
                    variant="secondary"
                    size="icon"
                    className="rounded-full"
                  >
                    <Avatar>
                      <AvatarImage
                        src="https://scontent.fdvo5-1.fna.fbcdn.net/v/t39.30808-6/327453272_6480450331984457_5221426715715363680_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=VgHjmJmc2IMQ7kNvgENcrno&_nc_ht=scontent.fdvo5-1.fna&oh=00_AYBoKWDUKyLJqFD5o9UcPu_PwBbyn6Scc5d9RCNnfTqQQQ&oe=664C1ED6"
                        alt="@shadcn"
                      />
                      <AvatarFallback>SWM</AvatarFallback>
                    </Avatar>
                    <span className="sr-only">Toggle user menu</span>
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuLabel>My Account</DropdownMenuLabel>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem>Settings</DropdownMenuItem>
                  <DropdownMenuItem>Support</DropdownMenuItem>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem
                    onClick={() => {
                      navigate({
                        to: "/",
                      });
                    }}
                  >
                    Logout
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          </header>
        ) : null}
        <div>
          <Outlet />
        </div>
        <TanStackRouterDevtools />
      </>
    );
  },
});
