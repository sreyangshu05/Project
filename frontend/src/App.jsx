import React, { useEffect } from 'react';
import { Container, Box, Typography } from '@mui/material';
import { useSelector, useDispatch } from 'react-redux';
import ChatHistory from './components/ChatHistory';
import ChatInput from './components/ChatInput';
import { loadMessages } from './redux/actions/chatActions';

const App = () => {
  const dispatch = useDispatch();
  const chatHistory = useSelector((state) => state.chatHistory);

  useEffect(() => {
    dispatch(loadMessages());
  }, [dispatch]);

  return (
    <Container maxWidth="sm" sx={{ padding: '20px' }}>
      <Box sx={{ padding: '20px', border: '1px solid #ddd', borderRadius: '8px' }}>
        <Typography variant="h4" gutterBottom>
          Chatbot
        </Typography>
        <ChatHistory chatHistory={chatHistory} />
        <ChatInput />
      </Box>
    </Container>
  );
};

export default App;
