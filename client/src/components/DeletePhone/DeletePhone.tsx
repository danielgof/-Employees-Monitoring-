import { useState } from 'react'
import Card from 'react-bootstrap/Card';
import CloseButton from 'react-bootstrap/CloseButton';
import serverURL from '../../libs/serverApi';

const DeletePhone = (props: any) => {
  const [message, setMessage] = useState("");
  const handleClick = async (e: any) => {
    e.preventDefault();
    try {
      const body = JSON.stringify({
        phone: props.phone
      })

      const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        phone: props.phone
      }))
      let res = await fetch(serverURL + "/api/v1/delete_phone", {
        method: "DELETE",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setMessage(`Телефон был удален из базы данных`);
        // navigate("/home");
      }
      else {
        setMessage("Произошла ошибка при удалении телефона");
      }
    } catch (err) {
      console.log(err);
    }
  }
  return (
    <Card className='container'>
      <Card.Title>
        <CloseButton className='delete-phone'
          onClick={handleClick} />
      </Card.Title>
      <div className="message">{message ? <p>{message}</p> : null}</div>
    </Card>
  );
}
export default DeletePhone;