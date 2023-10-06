import Button from 'react-bootstrap/Button';



export const Welcome = () => {

  return (
    <div className="bg-slate-600 p-4 border rounded-lg shadow-md text-center mx-auto max-w-md mt-20">
    <h1 className="text-3xl text-white">Welcome!</h1>
    <Button variant="primary">Primary</Button>{' '}
  </div>
);
};