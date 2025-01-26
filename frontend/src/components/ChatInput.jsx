import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import { useDispatch } from 'react-redux';
import { setUserInput, addMessage } from '../redux/actions/chatActions';
import axios from '../services/api';

const ChatInput = () => {
  const [input, setInput] = useState('');
  const dispatch = useDispatch();

  const handleSend = async () => {
    if (!input.trim()) return;

    // Dispatch user input
    dispatch(addMessage({ sender: 'user', message: input }));
    dispatch(setUserInput(input));

    // Send to backend
    try {
      const response = await axios.post('/chat', { query: input });
      if (response.data.response) {
        dispatch(addMessage({ sender: 'bot', message: response.data.response }));
      } else {
        dispatch(addMessage({ sender: 'bot', message: 'No response from chatbot.' }));
      }
    } catch (error) {
      dispatch(addMessage({ sender: 'bot', message: 'Error fetching response. Try again later.' }));
    }

    setInput('');
  };

  return (
    <div>
      <TextField
        fullWidth
        variant="outlined"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask a question..."
        sx={{ marginBottom: '10px' }}
      />
      <Button variant="contained" color="primary" onClick={handleSend}>
        Send
      </Button>
    </div>
  );
};

export default ChatInput;
