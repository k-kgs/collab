import { BaseAuthLayout } from "../../components/user/base";
import { LoginForm } from "../../components/user/login";
import Link from "next/link";

const styles = {
  marginTop: 30,
  textAlign: "center",
};
export default function Login() {
  return (
    <BaseAuthLayout>
      <LoginForm />

      <div style={styles}>
        <Link href="/user/register">Signup now!</Link>
      </div>
    </BaseAuthLayout>
  );
}
