#!/path/to/ruby/bin/ruby

$: << '/path/to/ruby/gem/gems/oauth-0.4.5/lib'

require 'open-uri'
require 'rexml/document'
require 'kconv'
require 'fileutils'

require 'rubygems'
require 'oauth'

$KCODE = 'UTF-8'

class DOCU
  # INIT
  private
    def init
      begin
        # ADD YOURS HERE
        msg = generateMsg
        res = postTwitter(msg)
        # ADD YOURS HERE
      end
    rescue => e
      p e
    end
  end
  # GENERATE message
  def generateMsg
    msg = ''
    return msg.toutf8
  end
  # POST to Twitter Account
  def postTwitter(message)
    begin
      # NOTICE: change your api Access level to Read and Write
      ckey = 'Consumer key'
      csec = 'Consumer secret'
      atkn = 'Access token'
      atsc = 'Access token secret'
      consumer = OAuth::Consumer.new(ckey, csec, :site => 'http://twitter.com')
      access_token = OAuth::AccessToken.new(consumer, atkn, atsc)
      response = access_token.post('http://twitter.com/statuses/update.json', 'status' => message)
    rescue => e
      p e
    end
  end
  public
  # EXECUTE (ENTRYPOINT)
  def execute
  	init
  end
end

d = DOCU.new()
d.execute