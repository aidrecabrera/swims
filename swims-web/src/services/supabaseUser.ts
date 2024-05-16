import { User } from "@supabase/supabase-js";
import { useEffect, useState } from "react";
import { supabase } from "./supabaseClient";

export const useSupabaseUser = () => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const fetchSession = async () => {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      if (session) {
        if (JSON.stringify(user) !== JSON.stringify(session.user)) {
          setUser(session.user);
        }
      } else {
        setUser(null);
      }
    };

    fetchSession();
  }, [supabase, user]);

  return user;
};

export type SupbaseSessionContext = ReturnType<typeof useSupabaseUser>;
