import { useState } from 'react';
import Card from 'react-bootstrap/Card';
import CloseButton from 'react-bootstrap/CloseButton';

const DeleteDepartment = (props: any) => {
  const [message, setMessage] = useState("");
  const handleClick = async (e: any) => {
    e.preventDefault();
    try {
    const body = JSON.stringify({
      id: props.id
    })

    const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        id: props.id
      }))
      let res = await fetch("http://127.0.0.1:5000/api/v1/delete_position", {
        method: "DELETE",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setMessage(`Должность ${props.position} была удалена из базы данных`);
        let n: number;
        n = window.setTimeout(function () { /* snip */  }, 50000);
        window.location.reload();
      } 
      else {
        setMessage("Произошла ошибка при удалении должности");
      }
    } catch (err) {
      console.log(err);
    }
  }
  return (
    <Card className='container'>
        <Card.Title>
          <CloseButton className='delete-position'
          onClick={handleClick} />
        </Card.Title>
        <div className="message">{message ? <p>{message}</p> : null}</div>
    </Card>
  );
}

export default DeleteDepartment;