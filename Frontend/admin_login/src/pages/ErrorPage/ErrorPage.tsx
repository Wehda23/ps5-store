import { useRouteError } from "react-router-dom";

export default function ErrorPage(): JSX.Element {
  const error: any = useRouteError();
  console.error(error);

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-4">Oops!</h1>
        <p className="text-lg mb-2">Sorry, an unexpected error has occurred.</p>
        <p className="text-sm text-gray-500">
          <i>{error.statusText || error.message}</i>
        </p>
      </div>
    </div>
  );
}
