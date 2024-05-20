import { BaseAuthLayout } from "../../components/user/base";
import { RegisterForm } from "../../components/user/register";
import Link from "next/link";

const styles = {
  marginTop: 30,
  textAlign: "center",
};
export default function Register() {
  return (
    <BaseAuthLayout>
      <RegisterForm />

      <div style={styles}>
        <Link href="/user/login">Registered Before? Signin Now!</Link>
      </div>
    </BaseAuthLayout>
  );
}
