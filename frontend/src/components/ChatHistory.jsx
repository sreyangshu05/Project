import React from 'react';
import { Box, Typography } from '@mui/material';

const ChatHistory = ({ chatHistory }) => {
  return (
    <Box sx={{ maxHeight: '400px', overflowY: 'auto', padding: '10px' }}>
      {chatHistory.map((entry, index) => (
        <Box key={index} sx={{ marginBottom: '10px' }}>
          <Typography variant="body1" color={entry.sender === 'user' ? 'primary' : 'textSecondary'}>
            {entry.message}
          </Typography>
        </Box>
      ))}
    </Box>
  );
};

export default ChatHistory;
